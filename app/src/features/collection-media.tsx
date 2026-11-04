"use client";
import Link from "next/link";
import { useState } from "react";
import { X } from "lucide-react";
import type { LibraryItem, ReferenceMedia } from "@/contracts/library";
import { api } from "@/components/shared";
import { PackageLightbox } from "./package-detail";
import styles from "./screen-browser.module.css";
export interface CollectionMediaEntry {
  id: string;
  collectionId: string;
  referenceId: string;
  mediaId: string;
  addedAt: number;
  reference: LibraryItem | null;
  name: string;
  media: ReferenceMedia | null;
}
export function CollectionScreens({
  id,
  items,
  onChanged,
}: {
  id: string;
  items: CollectionMediaEntry[];
  onChanged: () => void;
}) {
  const [current, setCurrent] = useState<CollectionMediaEntry | null>(null),
    [busy, setBusy] = useState(""),
    [error, setError] = useState("");
  const available = items.filter(
    (
      item,
    ): item is CollectionMediaEntry & {
      reference: LibraryItem;
      media: ReferenceMedia;
    } => !!item.reference && !!item.media,
  );
  async function remove(item: CollectionMediaEntry) {
    setBusy(item.id);
    setError("");
    try {
      await api(`/api/collections/${id}/media`, {
        method: "DELETE",
        body: JSON.stringify({
          referenceId: item.referenceId,
          mediaId: item.mediaId,
        }),
      });
      onChanged();
    } catch (e) {
      setError((e as Error).message);
    } finally {
      setBusy("");
    }
  }
  return (
    <section style={{ marginBottom: 40 }}>
      <div className="section-heading">
        <h2>Screens</h2>
        <span className="muted small-text">{items.length} saved</span>
      </div>
      {error && (
        <p className="error-text" role="alert">
          {error}
        </p>
      )}
      {!items.length ? (
        <p className="muted">
          Save a screenshot to this board from the screen viewer.{" "}
          <Link href="/library?view=screens">Browse screens</Link>
        </p>
      ) : (
        <div className={styles.grid}>
          {items.map((item) => (
            <article className={styles.card} key={item.id}>
              {item.media && item.reference ? (
                <>
                  <button
                    className={styles.open}
                    onClick={() => setCurrent(item)}
                    aria-label={`Open ${item.name}: ${item.media.name}`}
                  >
                    <div className={styles.picture}>
                      <img
                        src={item.media.thumbnail || item.media.url}
                        alt={item.media.name}
                        loading="lazy"
                      />
                    </div>
                  </button>
                  <div className={styles.caption}>
                    <strong>{item.name}</strong>
                    <button
                      className="text-button"
                      disabled={busy === item.id}
                      onClick={() => remove(item)}
                      aria-label={`Remove ${item.media.name} from board`}
                    >
                      <X size={14} />
                      Remove
                    </button>
                  </div>
                  <p>{item.media.name}</p>
                </>
              ) : (
                <p className="notice">Capture unavailable: {item.mediaId}</p>
              )}
            </article>
          ))}
        </div>
      )}
      {current?.reference && current.media && (
        <PackageLightbox
          detail={current.reference}
          current={current.media}
          items={available.map((item) => item.media)}
          onClose={() => setCurrent(null)}
          onChange={(media) =>
            setCurrent(available.find((item) => item.media === media) || null)
          }
        />
      )}
    </section>
  );
}
