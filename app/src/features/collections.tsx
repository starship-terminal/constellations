"use client";
import Link from "next/link";
import { useEffect, useState } from "react";
import {
  ArrowLeft,
  ArrowRight,
  BookOpen,
  Check,
  Download,
  Folder,
  FolderPlus,
  Pencil,
  Plus,
  Search,
  Trash2,
  X,
} from "lucide-react";
import type { LibraryItem } from "@/contracts/library";
import {
  api,
  Empty,
  ErrorState,
  MediaPreview,
  Modal,
  Spinner,
  useResource,
} from "@/components/shared";
import { ReferenceCard, ReferenceInspector } from "@/components/reference";
interface Collection {
  id: string;
  name: string;
  notes: string;
  createdAt: number;
  updatedAt: number;
}
interface CollectionEntry {
  referenceId: string;
  note: string;
  reference: LibraryItem | null;
  addedAt: number;
}
export function CollectionsPage() {
  const { data, setData, error, loading } = useResource<{
    collections: Collection[];
  }>("/api/collections");
  const [create, setCreate] = useState(false),
    [name, setName] = useState(""),
    [busy, setBusy] = useState(false),
    [localError, setError] = useState("");
  async function submit() {
    if (!name.trim()) return;
    setBusy(true);
    setError("");
    try {
      const d = await api("/api/collections", {
        method: "POST",
        body: JSON.stringify({ name: name.trim() }),
      });
      const c = d.collection || d;
      setData((prev) => ({ collections: [c, ...(prev?.collections || [])] }));
      setName("");
      setCreate(false);
    } catch (e) {
      setError((e as Error).message);
    } finally {
      setBusy(false);
    }
  }
  return (
    <div className="page collections-page">
      <header className="page-heading row-heading">
        <div>
          <h1>Bookmarks</h1>
          <p className="muted">
            A home for the references you want to return to.
          </p>
        </div>
        <button className="primary" onClick={() => setCreate(true)}>
          <Plus size={16} />
          New collection
        </button>
      </header>
      {loading ? (
        <Spinner label="Opening collections…" />
      ) : error ? (
        <ErrorState message={error} />
      ) : data?.collections.length ? (
        <div className="collections-grid">
          {data.collections.map((c) => (
            <Link
              className="collection-card"
              href={`/collections/${c.id}`}
              key={c.id}
            >
              <div className="collection-visual">
                <div className="collection-paper" />
                <div className="collection-paper" />
                <div className="collection-paper">
                  <Folder size={36} strokeWidth={1} />
                </div>
              </div>
              <div className="collection-card-title">
                <h2>{c.name}</h2>
                <ArrowRight size={17} />
              </div>
              <p>
                {c.notes
                  ? c.notes.slice(0, 110)
                  : "A considered collection of design references."}
              </p>
              <small>
                Updated{" "}
                {new Date(c.updatedAt).toLocaleDateString(undefined, {
                  month: "short",
                  day: "numeric",
                })}
              </small>
            </Link>
          ))}
        </div>
      ) : (
        <Empty title="Start a collection of good ideas.">
          <p>
            Save a reference from the library, or create a collection first.
          </p>
          <button className="primary" onClick={() => setCreate(true)}>
            <FolderPlus size={16} />
            Create a collection
          </button>
        </Empty>
      )}
      <Modal
        open={create}
        onOpenChange={setCreate}
        title="New collection"
        description="Give this direction a place to grow."
      >
        <form
          className="dialog-form"
          onSubmit={(e) => {
            e.preventDefault();
            submit();
          }}
        >
          <label>
            Name
            <input
              value={name}
              onChange={(e) => setName(e.target.value)}
              autoFocus
              maxLength={160}
              placeholder="e.g. A calmer kind of workspace"
              required
            />
          </label>
          {localError && (
            <p className="error-text" role="alert">
              {localError}
            </p>
          )}
          <button className="primary" disabled={busy}>
            {busy ? "Creating…" : "Create collection"}
          </button>
        </form>
      </Modal>
    </div>
  );
}
export function CollectionDetailPage({ id }: { id: string }) {
  const { data, setData, loading, error } = useResource<{
    collection: Collection;
    items: CollectionEntry[];
  }>(`/api/collections/${id}`);
  const [notes, setNotes] = useState(""),
    [name, setName] = useState(""),
    [rename, setRename] = useState(false),
    [adding, setAdding] = useState(false),
    [inspecting, setInspecting] = useState<LibraryItem | null>(null),
    [busy, setBusy] = useState(false),
    [saved, setSaved] = useState(false),
    [localError, setError] = useState("");
  useEffect(() => {
    if (data) {
      setNotes(data.collection.notes);
      setName(data.collection.name);
    }
  }, [data?.collection.id]);
  async function update(patch: { name?: string; notes?: string }) {
    setBusy(true);
    setError("");
    try {
      const d = await api(`/api/collections/${id}`, {
        method: "PATCH",
        body: JSON.stringify(patch),
      });
      setData((prev) =>
        prev ? { ...prev, collection: { ...prev.collection, ...patch } } : prev,
      );
      setRename(false);
      setSaved(true);
      setTimeout(() => setSaved(false), 2000);
    } catch (e) {
      setError((e as Error).message);
    } finally {
      setBusy(false);
    }
  }
  async function remove(referenceId: string) {
    setError("");
    try {
      await api(
        `/api/collections/${id}/items?referenceId=${encodeURIComponent(referenceId)}`,
        { method: "DELETE" },
      );
      setData((prev) =>
        prev
          ? {
              ...prev,
              items: prev.items.filter((x) => x.referenceId !== referenceId),
            }
          : prev,
      );
    } catch (e) {
      setError((e as Error).message);
    }
  }
  if (loading) return <Spinner label="Opening collection…" />;
  if (error || !data)
    return (
      <div className="page">
        <ErrorState message={error || "Collection not found."} />
        <Link href="/collections" className="pill">
          Back to collections
        </Link>
      </div>
    );
  const refs = data.items
    .map((x) => x.reference)
    .filter((x): x is LibraryItem => !!x);
  return (
    <div className="page collection-detail">
      <Link href="/collections" className="back-link">
        <ArrowLeft size={14} />
        All collections
      </Link>
      <header className="page-heading row-heading">
        <div>
          <div className="eyebrow">A collected direction</div>
          <h1>{data.collection.name}</h1>
          <p className="muted">
            {data.items.length} reference{data.items.length === 1 ? "" : "s"} ·
            Updated {new Date(data.collection.updatedAt).toLocaleDateString()}
          </p>
        </div>
        <div className="inline-actions">
          <button
            className="pill"
            onClick={() => setRename(true)}
            aria-label="Rename collection"
          >
            <Pencil size={14} />
            Rename
          </button>
          <a className="pill" href={`/api/collections/${id}/export`} download>
            <Download size={14} />
            Export
          </a>
          <button className="primary" onClick={() => setAdding(true)}>
            <Plus size={16} />
            Add reference
          </button>
        </div>
      </header>
      <section className="collection-notes">
        <label htmlFor="collection-notes">
          The thinking behind this collection
        </label>
        <textarea
          id="collection-notes"
          rows={3}
          value={notes}
          onChange={(e) => setNotes(e.target.value)}
          placeholder="What connects these references? What are you noticing?"
        />
        <div className="notes-footer">
          <span className="muted small-text">
            Keep a little context for your future self.
          </span>
          <button
            className="pill small"
            onClick={() => update({ notes })}
            disabled={busy || notes === data.collection.notes}
          >
            {saved ? <Check size={14} /> : null}
            {saved ? "Saved" : busy ? "Saving…" : "Save notes"}
          </button>
        </div>
      </section>
      {localError && <ErrorState message={localError} />}
      <div className="section-heading collection-section-heading">
        <h2>Your references</h2>
        <span className="muted small-text">{data.items.length} saved</span>
      </div>
      {data.items.length ? (
        <div className="reference-grid collection-reference-grid">
          {data.items.map((entry) => (
            <div key={entry.referenceId} className="saved-reference">
              {entry.reference ? (
                <ReferenceCard item={entry.reference} onOpen={setInspecting} />
              ) : (
                <div className="notice">
                  This reference is no longer available: {entry.referenceId}
                </div>
              )}
              <ItemNote id={id} entry={entry} />
              <button
                className="remove-reference text-button"
                onClick={() => remove(entry.referenceId)}
              >
                <X size={12} />
                Remove from collection
              </button>
            </div>
          ))}
        </div>
      ) : (
        <Empty title="The first reference sets the direction.">
          <p>Choose something that gives this collection a point of view.</p>
          <button className="pill" onClick={() => setAdding(true)}>
            <Plus size={16} />
            Find a reference
          </button>
        </Empty>
      )}
      <Modal open={rename} onOpenChange={setRename} title="Rename collection">
        <form
          className="dialog-form"
          onSubmit={(e) => {
            e.preventDefault();
            update({ name: name.trim() });
          }}
        >
          <label>
            Name
            <input
              value={name}
              onChange={(e) => setName(e.target.value)}
              maxLength={160}
              required
              autoFocus
            />
          </label>
          {localError && (
            <p role="alert" className="error-text">
              {localError}
            </p>
          )}
          <button className="primary" disabled={busy}>
            Save name
          </button>
        </form>
      </Modal>
      {adding && (
        <AddReferences
          id={id}
          existing={data.items.map((x) => x.referenceId)}
          onClose={() => setAdding(false)}
          onAdded={async () => {
            const d = await api(`/api/collections/${id}`);
            setData(d);
          }}
        />
      )}
      <ReferenceInspector
        items={refs}
        current={inspecting}
        onChange={setInspecting}
        onClose={() => setInspecting(null)}
      />
    </div>
  );
}
function ItemNote({ id, entry }: { id: string; entry: CollectionEntry }) {
  const [value, setValue] = useState(entry.note),
    [saved, setSaved] = useState(entry.note),
    [busy, setBusy] = useState(false),
    [error, setError] = useState("");
  async function save() {
    setBusy(true);
    try {
      await api(`/api/collections/${id}/items`, {
        method: "POST",
        body: JSON.stringify({ referenceId: entry.referenceId, note: value }),
      });
      setSaved(value);
    } catch (e) {
      setError((e as Error).message);
    } finally {
      setBusy(false);
    }
  }
  return (
    <div className="item-note">
      <textarea
        aria-label={`Note for ${entry.reference?.name || entry.referenceId}`}
        value={value}
        onChange={(e) => setValue(e.target.value)}
        rows={2}
        placeholder="Why did this catch your eye?"
      />
      {value !== saved && (
        <button className="pill small" onClick={save} disabled={busy}>
          {busy ? "Saving…" : "Save note"}
        </button>
      )}
      {error && (
        <p role="alert" className="error-text">
          {error}
        </p>
      )}
    </div>
  );
}
function AddReferences({
  id,
  existing,
  onClose,
  onAdded,
}: {
  id: string;
  existing: string[];
  onClose: () => void;
  onAdded: () => void;
}) {
  const [q, setQ] = useState(""),
    [query, setQuery] = useState(""),
    [added, setAdded] = useState(existing),
    [error, setError] = useState(""),
    [busy, setBusy] = useState("");
  useEffect(() => {
    const t = setTimeout(() => setQuery(q), 250);
    return () => clearTimeout(t);
  }, [q]);
  const { data, loading } = useResource<{ items: LibraryItem[] }>(
    `/api/library?q=${encodeURIComponent(query)}&limit=16`,
  );
  async function add(item: LibraryItem) {
    setBusy(item.id);
    try {
      await api(`/api/collections/${id}/items`, {
        method: "POST",
        body: JSON.stringify({ referenceId: item.id }),
      });
      setAdded((x) => [...x, item.id]);
      onAdded();
    } catch (e) {
      setError((e as Error).message);
    } finally {
      setBusy("");
    }
  }
  return (
    <Modal
      open={true}
      onOpenChange={(v) => {
        if (!v) onClose();
      }}
      title="Add references"
      description="Find something that belongs in this collection."
      className="add-references-modal"
    >
      <div className="search-field">
        <Search size={17} />
        <input
          autoFocus
          value={q}
          onChange={(e) => setQ(e.target.value)}
          aria-label="Search references to add"
          placeholder="Search the library…"
        />
      </div>
      {error && (
        <p className="error-text" role="alert">
          {error}
        </p>
      )}
      <div className="add-reference-list">
        {loading ? (
          <Spinner />
        ) : (
          data?.items.map((item) => (
            <div className="add-reference-row" key={item.id}>
              {item.icon ? (
                <img src={item.icon} alt="" />
              ) : (
                <span className="reference-letter">{item.name[0]}</span>
              )}
              <div>
                <strong>{item.name}</strong>
                <small>
                  {item.platform} · {item.evidence}
                </small>
              </div>
              <button
                className="pill small"
                onClick={() => add(item)}
                disabled={added.includes(item.id) || busy === item.id}
              >
                {added.includes(item.id) ? (
                  <Check size={14} />
                ) : (
                  <Plus size={14} />
                )}{" "}
                {added.includes(item.id)
                  ? "Added"
                  : busy === item.id
                    ? "Adding…"
                    : "Add"}
              </button>
            </div>
          ))
        )}
        {!loading && data?.items.length === 0 && (
          <Empty title="No references found." />
        )}
      </div>
    </Modal>
  );
}
