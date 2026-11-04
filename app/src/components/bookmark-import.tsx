"use client";
import { useEffect, useState } from "react";
import { api } from "./shared";
export function BookmarkImport() {
  const [value, setValue] = useState(""),
    [busy, setBusy] = useState(false),
    [status, setStatus] = useState(""),
    [detected, setDetected] = useState(0);
  // The old app shares this origin, so its browser bookmarks are readable here.
  useEffect(() => {
    try {
      const raw = localStorage.getItem("ds-saved");
      const paths: unknown = raw && JSON.parse(raw);
      if (
        Array.isArray(paths) &&
        paths.length &&
        paths.every((p) => typeof p === "string")
      ) {
        setValue(raw || "");
        setDetected(paths.length);
      }
    } catch {}
  }, []);
  return (
    <section className="settings-section">
      <div className="settings-section-label">
        <div>
          <h2>Import old screenshot bookmarks</h2>
          <p>
            The old app stores saved images in its browser, separately from this
            workspace.
          </p>
        </div>
      </div>
      <div className="settings-form">
        <p className="muted">
          Paste the JSON array from the old app’s local storage entry{" "}
          <code>ds-saved</code>. Only images that match this library are
          imported. Existing bookmarks stay saved.
        </p>
        {detected > 0 && (
          <p className="muted">
            Found {detected} saved image paths from the old app in this browser,
            prefilled below.
          </p>
        )}
        <label>
          Saved image paths
          <textarea
            rows={4}
            value={value}
            onChange={(e) => setValue(e.target.value)}
            placeholder={'["/media/systems/linear/screenshots/example.png"]'}
          />
        </label>
        <button
          className="pill"
          disabled={busy || !value.trim()}
          onClick={async () => {
            setBusy(true);
            setStatus("");
            try {
              const paths: unknown = JSON.parse(value);
              if (
                !Array.isArray(paths) ||
                !paths.every((p) => typeof p === "string")
              )
                throw new Error("Paste a JSON array of saved image paths.");
              const result = await api<{ imported: number; skipped: string[] }>(
                "/api/saved-media/import",
                { method: "POST", body: JSON.stringify({ paths }) },
              );
              setStatus(
                `Imported ${result.imported} saved images. ${result.skipped.length} unmatched paths skipped.`,
              );
              window.dispatchEvent(new Event("saved-media-changed"));
            } catch (e) {
              setStatus((e as Error).message);
            } finally {
              setBusy(false);
            }
          }}
        >
          {busy ? "Importing…" : "Import bookmarks"}
        </button>
        {status && <p role="status">{status}</p>}
      </div>
    </section>
  );
}
