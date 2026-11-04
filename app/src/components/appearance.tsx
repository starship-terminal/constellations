"use client";
import { useEffect, useState } from "react";
type Theme = "dark" | "light" | "system";
function apply(theme: Theme) {
  document.documentElement.dataset.theme =
    theme === "system"
      ? matchMedia("(prefers-color-scheme: dark)").matches
        ? "dark"
        : "light"
      : theme;
}
export function AppearanceBootstrap() {
  useEffect(() => {
    const update = () =>
      apply((localStorage.getItem("studio-theme") as Theme) || "dark");
    const media = matchMedia("(prefers-color-scheme: dark)");
    update();
    media.addEventListener("change", update);
    window.addEventListener("studio-appearance", update);
    return () => {
      media.removeEventListener("change", update);
      window.removeEventListener("studio-appearance", update);
    };
  }, []);
  return null;
}
export function AppearanceSettings() {
  const [theme, setTheme] = useState<Theme>("dark");
  useEffect(() => {
    setTheme((localStorage.getItem("studio-theme") as Theme) || "dark");
  }, []);
  return (
    <section className="settings-section">
      <div className="settings-section-label">
        <div>
          <h2>Appearance</h2>
          <p>Choose the workspace theme.</p>
        </div>
      </div>
      <label>
        Theme
        <select
          value={theme}
          onChange={(e) => {
            const value = e.target.value as Theme;
            setTheme(value);
            localStorage.setItem("studio-theme", value);
            window.dispatchEvent(new Event("studio-appearance"));
          }}
        >
          <option value="dark">Dark</option>
          <option value="light">Light</option>
          <option value="system">System</option>
        </select>
      </label>
    </section>
  );
}
