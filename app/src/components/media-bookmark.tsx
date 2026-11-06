"use client";
import { useEffect, useState, useSyncExternalStore } from "react";
import { Bookmark } from "lucide-react";
import { mediaDetailHref } from "@/features/package-detail-data";
import { api } from "./shared";
import type { ReferenceMedia } from "@/contracts/library";
interface Saved {
  referenceId: string;
  mediaId: string;
  name: string;
  media: ReferenceMedia | null;
  savedAt: number;
}
let items: Saved[] = [];
let pending: Promise<void> | undefined;
const empty: Saved[] = [];
const listeners = new Set<() => void>();
const subscribe = (fn: () => void) => {
  listeners.add(fn);
  return () => {
    listeners.delete(fn);
  };
};
function refresh() {
  if (!pending)
    pending = api<{ items: Saved[] }>("/api/saved-media")
      .then((data) => {
        items = data.items;
        listeners.forEach((fn) => fn());
      })
      .finally(() => {
        pending = undefined;
      });
  return pending;
}
function useSaved() {
  const rows = useSyncExternalStore(
    subscribe,
    () => items,
    () => empty,
  );
  const [error, setError] = useState("");
  useEffect(() => {
    const reload = () => {
      refresh().catch((e) => setError(e.message));
    };
    reload();
    window.addEventListener("saved-media-changed", reload);
    return () => window.removeEventListener("saved-media-changed", reload);
  }, []);
  return { rows, error };
}
export function MediaBookmarkButton({
  referenceId,
  mediaId,
  compact = false,
}: {
  referenceId: string;
  mediaId: string;
  compact?: boolean;
}) {
  const { rows } = useSaved();
  const saved = rows.some(
    (row) => row.referenceId === referenceId && row.mediaId === mediaId,
  );
  const [busy, setBusy] = useState(false),
    [error, setError] = useState("");
  return (
    <>
      <button
        className={compact ? "icon-button" : "pill small"}
        aria-label={saved ? "Unsave screenshot" : "Save screenshot"}
        aria-pressed={saved}
        disabled={busy}
        title={saved ? "Unsave screenshot" : "Save screenshot"}
        onClick={async () => {
          setBusy(true);
          setError("");
          try {
            await api("/api/saved-media", {
              method: saved ? "DELETE" : "POST",
              body: JSON.stringify({ referenceId, mediaId }),
            });
            if (pending) await pending.catch(() => {});
            await refresh();
          } catch (e) {
            setError((e as Error).message);
          } finally {
            setBusy(false);
          }
        }}
      >
        <Bookmark size={16} fill={saved ? "currentColor" : "none"} />
        {!compact && (saved ? "Saved" : "Save screenshot")}
      </button>
      {error && (
        <span role="alert" className="error-text">
          {error}
        </span>
      )}
    </>
  );
}
export function SavedMedia() {
  const { rows, error } = useSaved();
  return (
    <section style={{ marginTop: 32 }}>
      <h2>Saved screenshots</h2>
      <p className="muted">Individual captures you saved from a package.</p>
      {error && <p role="alert">{error}</p>}
      {!rows.length ? (
        <p className="muted">
          Open a gallery package and save a screenshot to keep it here.
        </p>
      ) : (
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fill,minmax(220px,1fr))",
            gap: 20,
          }}
        >
          {rows.map((row) => (
            <article key={`${row.referenceId}:${row.mediaId}`}>
              <a
                href={
                  row.referenceId.startsWith("refero:")
                    ? `/styles/refero/${row.referenceId.slice(7)}`
                    : row.media
                      ? mediaDetailHref(row.referenceId.slice(8), row.media)
                      : `/library/${row.referenceId.slice(8)}`
                }
              >
                <div
                  style={{
                    height: 180,
                    overflow: "hidden",
                    background: "var(--surface)",
                  }}
                >
                  {row.media?.type === "image" ? (
                    <img
                      src={row.media.url}
                      alt={row.media.name}
                      style={{
                        width: "100%",
                        height: "100%",
                        objectFit: "contain",
                      }}
                    />
                  ) : (
                    <span>{row.media ? "Video" : "Capture unavailable"}</span>
                  )}
                </div>
                <h3>{row.name}</h3>
              </a>
              <p className="muted">{row.media?.name || row.mediaId}</p>
              <MediaBookmarkButton
                referenceId={row.referenceId}
                mediaId={row.mediaId}
              />
            </article>
          ))}
        </div>
      )}
    </section>
  );
}
