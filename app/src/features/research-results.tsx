"use client";
import Link from "next/link";
import { useState } from "react";
import { ChevronDown, ChevronRight, Pin, Search } from "lucide-react";
import type { LibraryItem } from "@/contracts/library";
import { ReferenceCard, SaveReference } from "@/components/reference";
import styles from "./research-home.module.css";

/** Search activity remains visible while the answer develops, as on Refero.
 * Candidates are kept distinct from the model's inspected recommendations. */
export function ResearchResults({
  items,
  total,
  query,
  source,
  platform,
  theme,
  excluded,
  pinned,
  onInspect,
  onPin,
  onExclude,
}: {
  items: LibraryItem[];
  total: number;
  query?: string;
  source?: string;
  platform?: string;
  theme?: string;
  excluded: string[];
  pinned: string[];
  onInspect: (item: LibraryItem) => void;
  onPin: (id: string) => void;
  onExclude: (id: string) => void;
}) {
  const [limit, setLimit] = useState(6);
  const visible = items.filter((item) => !excluded.includes(item.id));
  const params = new URLSearchParams();
  if (query) params.set("q", query);
  if (platform) params.set("platform", platform);
  if (theme) params.set("theme", theme);
  // Styles and measured packages remain separate destinations.
  const href = source === "refero" ? `/styles?${params}` : `/library?${params}`;
  return (
    <section
      className={styles.searchResults}
      aria-label={query || "Library search results"}
    >
      <header className={styles.searchResultHeading}>
        <div>
          <span className={styles.searchResultKind}>
            <Search size={13} /> Library search
            {platform
              ? ` · ${platform === "mobile" ? "iOS apps" : platform === "desktop" ? "Desktop apps" : "Web apps"}`
              : ""}
          </span>
          <h3>{query || "References to explore"}</h3>
        </div>
        <div className={styles.searchDestinations}>
          <small>{total} references</small>
          {source ? (
            <Link href={href}>
              See all <ChevronRight size={15} />
            </Link>
          ) : (
            <>
              <Link href={`/library?${params}`}>
                Packages <ChevronRight size={15} />
              </Link>
              <Link href={`/styles?${params}`}>
                Styles <ChevronRight size={15} />
              </Link>
            </>
          )}
        </div>
      </header>
      {visible.length ? (
        <div className="research-result-grid">
          {visible.slice(0, limit).map((item) => (
            <div className="research-result" key={item.id}>
              <ReferenceCard item={item} onOpen={onInspect} />
              <div className="research-result-actions">
                <button
                  className={`pill small ${pinned.includes(item.id) ? "active" : ""}`}
                  onClick={() => onPin(item.id)}
                  aria-pressed={pinned.includes(item.id)}
                >
                  <Pin size={12} />
                  {pinned.includes(item.id) ? "Pinned" : "Pin"}
                </button>
                <SaveReference item={item} compact />
                <button
                  className="text-button"
                  onClick={() => onExclude(item.id)}
                >
                  Exclude
                </button>
              </div>
            </div>
          ))}
        </div>
      ) : (
        <p className="muted">
          {items.length
            ? "No remaining candidates in this batch. Restore an excluded reference or explore the full results."
            : "No references matched this search. Try another description."}
        </p>
      )}
      {visible.length > 6 && (
        <button
          className={styles.showMoreResults}
          onClick={() => setLimit(limit >= visible.length ? 6 : visible.length)}
          aria-expanded={limit > 6}
        >
          {limit > 6 ? "Show less" : "Show more"}
          <ChevronDown size={14} />
        </button>
      )}
    </section>
  );
}
