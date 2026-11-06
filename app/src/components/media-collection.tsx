"use client";
import Link from "next/link";
import { useEffect, useRef, useState } from "react";
import { Bookmark, Check, Folder, Plus, X } from "lucide-react";
import * as Dialog from "@radix-ui/react-dialog";
import { api, Spinner } from "./shared";
import styles from "./media-collection.module.css";
interface Board {
  id: string;
  name: string;
  mediaCount?: number;
}
export function MediaCollectionButton({
  referenceId,
  mediaId,
}: {
  referenceId: string;
  mediaId: string;
}) {
  return (
    <MediaCollectionPicker
      key={JSON.stringify([referenceId, mediaId])}
      referenceId={referenceId}
      mediaId={mediaId}
    />
  );
}
function MediaCollectionPicker({
  referenceId,
  mediaId,
}: {
  referenceId: string;
  mediaId: string;
}) {
  const trigger = useRef<HTMLButtonElement | null>(null);
  const live = useRef(true);
  useEffect(() => {
    live.current = true;
    return () => {
      live.current = false;
    };
  }, []);
  const [open, setOpen] = useState(false),
    [boards, setBoards] = useState<Board[]>([]),
    [memberships, setMemberships] = useState<string[]>([]),
    [loading, setLoading] = useState(false),
    [busy, setBusy] = useState(""),
    [name, setName] = useState(""),
    [creating, setCreating] = useState(false),
    [error, setError] = useState("");
  useEffect(() => {
    if (!open) return;
    let alive = true;
    setLoading(true);
    setError("");
    api<{ collections: Board[]; mediaCollectionIds?: string[] }>(
      `/api/collections?referenceId=${encodeURIComponent(referenceId)}&mediaId=${encodeURIComponent(mediaId)}`,
    )
      .then((value) => {
        if (alive) {
          setBoards(value.collections);
          setMemberships(value.mediaCollectionIds || []);
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
  }, [open, referenceId, mediaId]);
  async function save(board: Board) {
    if (memberships.includes(board.id)) return;
    if (live.current) {
      setBusy(board.id);
      setError("");
    }
    try {
      await api(`/api/collections/${board.id}/media`, {
        method: "POST",
        body: JSON.stringify({ referenceId, mediaId }),
      });
      window.dispatchEvent(new Event("collection-media-changed"));
      if (!live.current) return;
      setMemberships((previous) => [...previous, board.id]);
      setBoards((previous) =>
        previous.map((row) =>
          row.id === board.id
            ? { ...row, mediaCount: (row.mediaCount || 0) + 1 }
            : row,
        ),
      );
    } catch (e) {
      if (live.current) setError((e as Error).message);
    } finally {
      if (live.current) setBusy("");
    }
  }
  async function create() {
    if (!name.trim()) return;
    setBusy("new");
    setError("");
    try {
      const board = await api<Board>("/api/collections", {
        method: "POST",
        body: JSON.stringify({ name: name.trim() }),
      });
      if (live.current) {
        setBoards((previous) => [board, ...previous]);
        setName("");
        setCreating(false);
      }
      // Finish the requested Create & save even if the user navigates away.
      // Only UI feedback belongs to this mounted capture picker.
      await save(board);
    } catch (e) {
      if (live.current) setError((e as Error).message);
    } finally {
      if (live.current) setBusy("");
    }
  }
  return (
    <>
      <button
        ref={trigger}
        className="pill"
        onClick={() => setOpen(true)}
        aria-label="Save screenshot to board"
      >
        <Bookmark size={16} />
        Save to…
      </button>
      <Dialog.Root
        open={open}
        onOpenChange={(value) => {
          setOpen(value);
          if (!value) {
            setCreating(false);
            setName("");
            setError("");
          }
        }}
      >
        <Dialog.Portal>
          <Dialog.Overlay className={`modal-overlay ${styles.overlay}`} />
          <Dialog.Content
            className={`modal ${styles.dialog}`}
            onCloseAutoFocus={(event) => {
              event.preventDefault();
              trigger.current?.focus();
            }}
          >
            <header className="modal-header">
              <div>
                <Dialog.Title>Save screenshot</Dialog.Title>
                <Dialog.Description>
                  Choose a board for this capture.
                </Dialog.Description>
              </div>
              <Dialog.Close className="icon-button" aria-label="Close">
                <X size={20} />
              </Dialog.Close>
            </header>
            <div className={styles.heading}>
              <strong>Boards</strong>
              <button
                className="text-button"
                onClick={() => setCreating((value) => !value)}
              >
                <Plus size={15} />
                Add board
              </button>
            </div>
            {creating && (
              <form
                className={styles.create}
                onSubmit={(event) => {
                  event.preventDefault();
                  create();
                }}
              >
                <input
                  aria-label="Board name"
                  value={name}
                  onChange={(event) => setName(event.target.value)}
                  placeholder="Board name"
                  maxLength={160}
                  required
                  autoFocus
                />
                <button className="primary small" disabled={!!busy}>
                  {busy === "new" ? "Creating…" : "Create & save"}
                </button>
                <button
                  type="button"
                  className="pill small"
                  disabled={!!busy}
                  onClick={() => {
                    setCreating(false);
                    setName("");
                  }}
                >
                  Cancel
                </button>
              </form>
            )}
            {error && (
              <p className="error-text" role="alert">
                {error}
              </p>
            )}
            {loading ? (
              <Spinner label="Opening boards…" />
            ) : (
              <div className={styles.boards}>
                {boards.map((board) => (
                  <button
                    key={board.id}
                    className={styles.board}
                    onClick={() => save(board)}
                    disabled={!!busy || memberships.includes(board.id)}
                    aria-label={`${memberships.includes(board.id) ? "Saved to" : "Save to"} ${board.name}`}
                  >
                    <Folder size={18} />
                    <span>
                      {board.name}
                      <small>
                        {board.mediaCount || 0}{" "}
                        {board.mediaCount === 1 ? "screen" : "screens"}
                      </small>
                    </span>
                    {memberships.includes(board.id) ? (
                      <Check size={18} />
                    ) : (
                      <Plus size={17} />
                    )}
                  </button>
                ))}
                {!boards.length && (
                  <p className="muted">
                    Create a board to keep this screenshot.
                  </p>
                )}
              </div>
            )}
            <Link className={styles.manage} href="/collections">
              View bookmarks
            </Link>
          </Dialog.Content>
        </Dialog.Portal>
      </Dialog.Root>
    </>
  );
}
